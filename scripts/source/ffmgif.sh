# This function is to be sourced in bashrc

# Example usage
# $ ffmgif -i input.mp4 -o output.mp4
ffmgif() {
    local input output

    while [[ ${1} ]]; do
        case "${1}" in
            -i)
                input=${2}
                shift
                ;;
            -o)
                output=${2}
                shift
                ;;
            *)
            echo "Error: Unknown parameter: ${1}" >&2
            return 1
        esac

        if ! shift; then
            echo "Missing parameter argument." >&2
            return 1
        fi
    done

    if [[ -z "$input" ]]; then
        echo "Error: input file is not specified" >&2
        return 1
    fi

    if [[ -z "$output" ]]; then
        echo "Error: output file is not specified" >&2
        return 1
    fi

    ffmpeg -i "$input" -r 15 -vf "split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" "$output"
}